"""
Sample test data for Digital Fatigue Manager
Use this to populate the database with test data for development/testing
"""

from backend.models.database import SessionLocal, Message, UserSettings, AgentDecision
from datetime import datetime, timedelta
import json

def create_sample_data():
    """Create sample messages and settings for testing"""
    db = SessionLocal()
    
    try:
        # Create default user settings if not exists
        settings = db.query(UserSettings).first()
        if not settings:
            settings = UserSettings(
                current_focus_mode="normal",
                working_hours_start="09:00",
                working_hours_end="17:00",
                working_days="mon,tue,wed,thu,fri",
                important_contacts=["boss@company.com", "team@company.com"],
                priority_keywords=["urgent", "deadline", "asap", "important", "critical"],
                notification_enabled=True,
                daily_summary_enabled=True,
                summary_time="18:00"
            )
            db.add(settings)
            db.commit()
        
        # Sample messages
        sample_messages = [
            {
                "source": "gmail",
                "sender": "boss@company.com",
                "content": "URGENT: Need the quarterly report by EOD. This is critical for the board meeting tomorrow.",
                "subject": "URGENT: Quarterly Report Needed",
                "timestamp": datetime.utcnow() - timedelta(hours=1),
                "priority_score": 9.5,
                "urgency_level": "high",
                "action": "SHOW",
                "final_decision": "SHOW",
                "confidence_score": 0.95,
                "priority_reasoning": "Important sender (4.0 points); Priority keywords detected: urgent, critical (2.5 points)",
                "context_explanation": "Recent message (< 1 hour)",
                "focus_justification": "Critical priority with high urgency",
                "supervisor_explanation": "Priority Score: 9.5/10 (Important sender + urgent keyword detected) | Urgency: HIGH | Final Decision: SHOW",
                "shown_to_user": True
            },
            {
                "source": "slack",
                "sender": "U123456",
                "content": "Hey team, just wanted to share some updates on the project. Nothing urgent, but wanted to keep everyone in the loop.",
                "channel": "C123456",
                "timestamp": datetime.utcnow() - timedelta(hours=3),
                "priority_score": 4.0,
                "urgency_level": "medium",
                "action": "SUMMARIZE",
                "final_decision": "SUMMARIZE",
                "confidence_score": 0.75,
                "priority_reasoning": "Standard priority - no high-priority indicators",
                "context_explanation": "Message age: 3.0 hours",
                "focus_justification": "Medium priority - add to daily summary",
                "supervisor_explanation": "Priority Score: 4.0/10 (Standard priority) | Urgency: MEDIUM | Final Decision: SUMMARIZE",
                "shown_to_user": False
            },
            {
                "source": "gmail",
                "sender": "newsletter@example.com",
                "content": "This week's newsletter: Top 10 productivity tips, latest industry news, and more!",
                "subject": "Weekly Newsletter - Productivity Tips",
                "timestamp": datetime.utcnow() - timedelta(hours=5),
                "priority_score": 2.0,
                "urgency_level": "low",
                "action": "HIDE",
                "final_decision": "HIDE",
                "confidence_score": 0.90,
                "priority_reasoning": "Standard priority - no high-priority indicators",
                "context_explanation": "Older message (5.0 hours)",
                "focus_justification": "Low priority 2.0 - hide from immediate view",
                "supervisor_explanation": "Priority Score: 2.0/10 (Standard priority) | Urgency: LOW | Final Decision: HIDE",
                "shown_to_user": False
            },
            {
                "source": "gmail",
                "sender": "team@company.com",
                "content": "Deadline reminder: Please submit your project updates by Friday. Thanks!",
                "subject": "Deadline Reminder - Project Updates",
                "timestamp": datetime.utcnow() - timedelta(hours=2),
                "priority_score": 7.0,
                "urgency_level": "high",
                "action": "SHOW",
                "final_decision": "SHOW",
                "confidence_score": 0.85,
                "priority_reasoning": "Important sender (4.0 points); Priority keywords detected: deadline (2.0 points)",
                "context_explanation": "Recent message (< 1 hour)",
                "focus_justification": "Priority 7.0 meets normal mode threshold (6.0)",
                "supervisor_explanation": "Priority Score: 7.0/10 (Important sender + deadline keyword) | Urgency: HIGH | Final Decision: SHOW",
                "shown_to_user": True
            },
            {
                "source": "slack",
                "sender": "U789012",
                "content": "Can you help me with the API integration? No rush, just whenever you have time.",
                "channel": "C789012",
                "timestamp": datetime.utcnow() - timedelta(minutes=30),
                "priority_score": 6.5,
                "urgency_level": "high",
                "action": "POSTPONE",
                "final_decision": "POSTPONE",
                "confidence_score": 0.70,
                "priority_reasoning": "Direct question/mention detected (2.0 points)",
                "context_explanation": "Recent message (< 1 hour)",
                "focus_justification": "Moderate priority with high urgency - postpone",
                "supervisor_explanation": "Priority Score: 6.5/10 (Direct question detected) | Urgency: HIGH | Final Decision: POSTPONE",
                "shown_to_user": False
            }
        ]
        
        # Add sample messages
        for msg_data in sample_messages:
            # Check if message already exists (by sender + timestamp)
            existing = db.query(Message).filter(
                Message.sender == msg_data["sender"],
                Message.timestamp == msg_data["timestamp"]
            ).first()
            
            if not existing:
                message = Message(**msg_data)
                db.add(message)
        
        db.commit()
        print("SUCCESS: Sample data created successfully!")
        print(f"   - Created/updated user settings")
        print(f"   - Created {len(sample_messages)} sample messages")
        
    except Exception as e:
        db.rollback()
        print(f"ERROR: Error creating sample data: {str(e)}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    create_sample_data()

