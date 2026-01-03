"""
Slack API Integration Service
"""
import hmac
import hashlib
import time
from typing import Dict, Any, Optional
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from backend.utils.config import Config
from backend.utils.logger import logger


class SlackService:
    """Service for Slack API integration"""
    
    def __init__(self):
        self.client = None
        self.bot_token = Config.SLACK_BOT_TOKEN
        self.signing_secret = Config.SLACK_SIGNING_SECRET
        
        if self.bot_token:
            self.client = WebClient(token=self.bot_token)
    
    def verify_signature(self, timestamp: str, body: str, signature: str) -> bool:
        """Verify Slack request signature"""
        if not self.signing_secret:
            return False
        
        # Check timestamp (reject if older than 5 minutes)
        if abs(time.time() - int(timestamp)) > 60 * 5:
            return False
        
        # Create signature
        sig_basestring = f"v0:{timestamp}:{body}"
        computed_signature = 'v0=' + hmac.new(
            self.signing_secret.encode(),
            sig_basestring.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return hmac.compare_digest(computed_signature, signature)
    
    def process_event(self, event: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Process Slack event (message events)"""
        try:
            event_type = event.get("type")
            
            # Handle URL verification challenge
            if event_type == "url_verification":
                return {"challenge": event.get("challenge")}
            
            # Handle event callbacks
            if event_type == "event_callback":
                inner_event = event.get("event", {})
                
                # Only process message events
                if inner_event.get("type") == "message" and "subtype" not in inner_event:
                    return {
                        "source": "slack",
                        "event": inner_event
                    }
            
            return None
        
        except Exception as e:
            logger.error(f"Error processing Slack event: {str(e)}")
            return None
    
    def get_user_info(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get user information from Slack"""
        if not self.client:
            return None
        
        try:
            response = self.client.users_info(user=user_id)
            return response.get("user", {})
        except SlackApiError as e:
            logger.error(f"Error fetching Slack user info: {str(e)}")
            return None
    
    def get_channel_info(self, channel_id: str) -> Optional[Dict[str, Any]]:
        """Get channel information from Slack"""
        if not self.client:
            return None
        
        try:
            response = self.client.conversations_info(channel=channel_id)
            return response.get("channel", {})
        except SlackApiError as e:
            logger.error(f"Error fetching Slack channel info: {str(e)}")
            return None

