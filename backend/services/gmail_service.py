"""
Gmail API Integration Service
"""
import os
import base64
from typing import List, Dict, Any, Optional
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from backend.utils.config import Config
from backend.utils.logger import logger

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class GmailService:
    """Service for Gmail API integration"""
    
    def __init__(self):
        self.credentials = None
        self.service = None
    
    def authenticate(self, token_file: str = "gmail_token.json") -> bool:
        """Authenticate with Gmail API using OAuth 2.0"""
        try:
            creds = None
            
            # Check if token exists
            if os.path.exists(token_file):
                creds = Credentials.from_authorized_user_file(token_file, SCOPES)
            
            # If no valid credentials, get new ones
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    # For production, you'd redirect to OAuth flow
                    # For development, use credentials.json
                    if not os.path.exists("credentials.json"):
                        logger.warning("credentials.json not found. Gmail authentication disabled.")
                        return False
                    
                    flow = InstalledAppFlow.from_client_secrets_file(
                        "credentials.json", SCOPES)
                    creds = flow.run_local_server(port=0)
                
                # Save credentials for next run
                with open(token_file, 'w') as token:
                    token.write(creds.to_json())
            
            self.credentials = creds
            self.service = build('gmail', 'v1', credentials=creds)
            return True
        
        except Exception as e:
            logger.error(f"Gmail authentication error: {str(e)}")
            return False
    
    def get_unread_messages(self, max_results: int = 10) -> List[Dict[str, Any]]:
        """Fetch unread messages from Gmail"""
        if not self.service:
            if not self.authenticate():
                return []
        
        try:
            # List messages
            results = self.service.users().messages().list(
                userId='me',
                q='is:unread',
                maxResults=max_results
            ).execute()
            
            messages = results.get('messages', [])
            
            # Get full message details
            full_messages = []
            for msg in messages:
                try:
                    message = self.service.users().messages().get(
                        userId='me',
                        id=msg['id']
                    ).execute()
                    full_messages.append(message)
                except HttpError as e:
                    logger.error(f"Error fetching message {msg['id']}: {str(e)}")
                    continue
            
            return full_messages
        
        except HttpError as e:
            logger.error(f"Gmail API error: {str(e)}")
            return []
        except Exception as e:
            logger.error(f"Error fetching Gmail messages: {str(e)}")
            return []
    
    def mark_as_read(self, message_id: str) -> bool:
        """Mark a message as read"""
        if not self.service:
            return False
        
        try:
            self.service.users().messages().modify(
                userId='me',
                id=message_id,
                body={'removeLabelIds': ['UNREAD']}
            ).execute()
            return True
        except Exception as e:
            logger.error(f"Error marking message as read: {str(e)}")
            return False

