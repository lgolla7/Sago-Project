import time
import json
from typing import List, Dict, Optional


class FollowUpAgent:
    def __init__(self):
        """
        Initializes the agent.
        In production, this would connect to a database and LLM provider.
        """
        
        self.watchlist: Dict[str, Dict] = {} 
        print(" Sago Agent Initialized. Ready to track.")

    def add_to_watchlist(self, email_thread: str):
        """
        INGESTION LAYER (Seamless Integration)
        Parses a forwarded rejection email to extract structured monitoring rules.
        """
        print("\n---  Parsing Incoming Email ---")
        
        
        extracted_data = {
            "company": "TechNova",
            "founder": "Sarah Chen",
            "founder_email": "sarah@technova.ai",
            "pass_reason": "Pre-revenue, product still in beta",
            "target_signals": ["Series A", "Official Launch", "Revenue Milestone"],
            "last_contact_date": "2023-11-15"
        }
        
        
        self.watchlist[extracted_data["company"]] = extracted_data
        print(f" Added to Watchlist: {extracted_data['company']}")
        print(f"   Reason for pass: '{extracted_data['pass_reason']}'")
        print(f"   Waiting for: {extracted_data['target_signals']}")

    def check_market_signals(self, company_name: str) -> List[str]:
        """
        INTELLIGENCE LAYER (Monitoring)
        Simulates scanning external sources (Crunchbase, TechCrunch) for news.
        """
        print(f"\n---  Scanning Market Signals for {company_name} ---")
        
       
        simulated_news = [
            "TechNova announces $12M Series A led by Sequoia",
            "TechNova releases public API v1.0"
        ]
       
        
        return simulated_news

    def evaluate_signal(self, company_data: Dict, news_events: List[str]) -> Optional[str]:
        """
        INTELLIGENCE LAYER (Relevance)
        Determines if the news specifically addresses the investor's 'pass reason'.
        """
        print(f"--- Evaluating Signal Relevance ---")
        
        
        for event in news_events:
            
            if "Series A" in event:
                print(f"   MATCH FOUND: '{event}' matches target 'Series A'.")
                return event
        
        return None

    def generate_draft(self, company_name: str, trigger_event: str) -> str:
        """
        ACTION LAYER (True Agency & Hyper-Personalization)
        Drafts the email to be placed in the user's Drafts folder.
        """
        data = self.watchlist[company_name]
        print("\n--- Generating Personalized Draft ---")
        
        
        email_draft = (
            f"To: {data['founder_email']}\n"
            f"Subject: Congrats on the Series A!\n\n"
            f"Hi {data['founder'].split()[0]},\n\n"
            f"I just saw the news about your {trigger_event.split('announces ')[1]}—huge congratulations.\n\n"
            f"When we last spoke in November, you mentioned you were focused on getting out of beta. "
            f"It's impressive to see how fast you've moved from '{data['pass_reason']}' to this major milestone.\n\n"
            f"I'd love to reconnect and hear how the roadmap looks now that you're capitalized. "
            f"Are you free next Tuesday?\n\n"
            f"Best,\n[Investor Name]"
        )
        
        
        return email_draft

    def run_daily_scan(self):
        """
        Orchestrator function to simulate the daily workflow.
        """
        for company, data in self.watchlist.items():
         
            news = self.check_market_signals(company)
            
            
            relevant_event = self.evaluate_signal(data, news)
            
            
            if relevant_event:
                draft = self.generate_draft(company, relevant_event)
                print("\n===  FINAL DRAFT CREATED (Saved to Gmail) ===")
                print(draft)
                print("=========")


if __name__ == "__main__":
  
    agent = FollowUpAgent()
    
   
    sample_email = """
    To: sarah@technova.ai
    From: me@sago.vc
    Subject: Re: Seed Round
    Hi Sarah, thanks for the chat. We are passing for now because it is too early. 
    Let's reconnect when you hit $1M ARR or raise your Series A.
    """
    agent.add_to_watchlist(sample_email)
    
    
    time.sleep(1)
    agent.run_daily_scan()