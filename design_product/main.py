import os
from crewai import Crew
from decouple import config
from agents import DesignAgents
from tasks import DesignTasks

# 设置环境变量
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = config("OPENAI_BASE_URL")
os.environ["MODEL_NAME"] = config("MODEL_NAME")

class DesignCrew:
    def __init__(self, product_area, problem_statement=None):
        self.product_area = product_area
        self.problem_statement = problem_statement
        
    def run(self):
        # 初始化agents和tasks
        agents = DesignAgents()
        tasks = DesignTasks()
        
        # 创建所有角色
        pm = agents.product_manager()
        designer = agents.design_strategist()
        tech = agents.technical_advisor()
        user_advocate = agents.user_advocate()
        
        # 定义任务流程
        task1 = tasks.define_problem(
            pm,
            self.product_area
        )
        
        task2 = tasks.generate_hmw(
            designer,
            self.problem_statement or "生成HMW"
        )
        
        task3 = tasks.evaluate_technical(
            tech,
            "评估技术方案"
        )
        
        task4 = tasks.collect_user_feedback(
            user_advocate,
            "用户代理人反馈"
        )
        
        # 创建crew
        crew = Crew(
            agents=[pm, designer, tech, user_advocate],
            tasks=[task1, task2, task3, task4],
            verbose=True
        )
        
        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## 欢迎使用产品设计系统")
    print("-------------------------------")
    product_area = input("请输入产品领域: ")
    
    crew = DesignCrew(product_area)
    result = crew.run()
    print("\n\n########################")
    print("## 设计流程输出结果:")
    print("########################\n")
    print(result) 