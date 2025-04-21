# agent.py
import time

def run_agent(goal):
    print(f"\n🧠 Goal received: {goal}")
    steps = plan_steps(goal)
    for step in steps:
        print(f"\n🔄 Step: {step}")
        result = act(step)
        print(f"✅ Result: {result}")
        reflect(step, result)
        time.sleep(1)
    print("\n🎉 Goal complete!")

def plan_steps(goal):
    # Very basic logic – simulate planning
    return [f"Research: {goal}", f"Write output for: {goal}", "Summarize results"]

def act(step):
    # Simulate doing something
    return f"Did '{step}' successfully."

def reflect(step, result):
    print(f"📝 Reflection on '{step}': Went well.")

if __name__ == "__main__":
    user_goal = input("Enter your goal for this AI agent: ")
    run_agent(user_goal)