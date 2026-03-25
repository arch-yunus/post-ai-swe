import asyncio
import uuid
from typing import List, Dict

class Agent:
    def __init__(self, name: str, role: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.role = role

    async def execute_task(self, task_description: str) -> str:
        print(f"[{self.name}] Executing role: {self.role} for task: {task_description}")
        await asyncio.sleep(1)  # Simulate intelligence work
        return f"Result from {self.name} ({self.role})"

class SwarmOrchestrator:
    def __init__(self):
        self.agents: List[Agent] = []
        self.history: List[Dict] = []

    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    async def broadcast_mission(self, mission: str):
        print(f"🚀 Mission Started: {mission}\n")
        tasks = [agent.execute_task(mission) for agent in self.agents]
        results = await asyncio.gather(*tasks)
        
        for agent, res in zip(self.agents, results):
            print(f"✅ {agent.name} returned: {res}")
            self.history.append({"agent": agent.name, "result": res})
        
        print(f"\n✨ Mission Completed. Total reports collected: {len(results)}")

async def main():
    orchestrator = SwarmOrchestrator()
    
    # Initialize a small swarm
    orchestrator.add_agent(Agent("Architect", "System Design & Decomposition"))
    orchestrator.add_agent(Agent("Coder", "Python/Rust Implementation"))
    orchestrator.add_agent(Agent("Reviewer", "Security & Quality Audit"))
    
    await orchestrator.broadcast_mission("Migrate legacy authentication module to OAuth2")

if __name__ == "__main__":
    asyncio.run(main())
