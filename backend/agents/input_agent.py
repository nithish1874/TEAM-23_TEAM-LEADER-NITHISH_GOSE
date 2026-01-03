"""
Input Agent - Collects and normalizes data from Gmail and Slack
"""
from datetime import datetime
from typing import Dict, Any
from backend.agents.base_agent import BaseAgent
from backend.utils.logger import logger


class InputAgent(BaseAgent):
    """Normalizes messages from different sources into a common format"""
    
    def __init__(self):
        super().__init__("InputAgent")
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalize message data from Gmail or Slack
        
        Args:
            input_data: Raw message data from API
            
        Returns:
            Normalized message format
        """
        try:
            source = input_data.get("source", "").lower()
            
            if source == "gmail":
                return self._normalize_gmail(input_data)
            elif source == "slack":
                return self._normalize_slack(input_data)
            else:
                raise ValueError(f"Unknown source: {source}")
        
        except Exception as e:
            logger.error(f"InputAgent error: {str(e)}")
            raise
    
    def _normalize_gmail(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize Gmail message"""
        # Extract email data
        message_data = data.get("message", {})
        payload = message_data.get("payload", {})
        headers = payload.get("headers", [])
        
        # Extract headers
        header_dict = {h["name"].lower(): h["value"] for h in headers}
        
        sender = header_dict.get("from", "unknown")
        subject = header_dict.get("subject", "")
        date_str = header_dict.get("date", "")
        
        # Parse body
        body = self._extract_gmail_body(payload)
        
        # Parse timestamp
        try:
            from email.utils import parsedate_to_datetime
            timestamp = parsedate_to_datetime(date_str) if date_str else datetime.utcnow()
        except:
            timestamp = datetime.utcnow()
        
        return {
            "source": "gmail",
            "sender": sender,
            "content": body,
            "timestamp": timestamp,
            "metadata": {
                "subject": subject,
                "message_id": message_data.get("id", ""),
                "thread_id": message_data.get("threadId", ""),
                "snippet": message_data.get("snippet", "")
            }
        }
    
    def _normalize_slack(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize Slack message"""
        event = data.get("event", {})
        
        sender = event.get("user", "unknown")
        content = event.get("text", "")
        channel = event.get("channel", "")
        ts = event.get("ts", "")
        thread_ts = event.get("thread_ts")
        
        # Parse timestamp (Slack ts is Unix timestamp as string)
        try:
            timestamp = datetime.fromtimestamp(float(ts)) if ts else datetime.utcnow()
        except:
            timestamp = datetime.utcnow()
        
        return {
            "source": "slack",
            "sender": sender,
            "content": content,
            "timestamp": timestamp,
            "metadata": {
                "channel": channel,
                "thread_ts": thread_ts,
                "event_type": event.get("type", ""),
                "event_id": event.get("event_ts", "")
            }
        }
    
    def _extract_gmail_body(self, payload: Dict[str, Any]) -> str:
        """Extract text body from Gmail payload"""
        body = ""
        
        # Check if it's multipart
        mime_type = payload.get("mimeType", "")
        
        if mime_type == "text/plain":
            body = payload.get("body", {}).get("data", "")
            if body:
                import base64
                body = base64.urlsafe_b64decode(body).decode("utf-8", errors="ignore")
        
        elif mime_type == "multipart/alternative" or mime_type == "multipart/mixed":
            parts = payload.get("parts", [])
            for part in parts:
                if part.get("mimeType") == "text/plain":
                    body_data = part.get("body", {}).get("data", "")
                    if body_data:
                        import base64
                        body = base64.urlsafe_b64decode(body_data).decode("utf-8", errors="ignore")
                        break
        
        return body or ""

