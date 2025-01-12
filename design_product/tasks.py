from crewai import Task
from textwrap import dedent

class DesignTasks:
    def __tip_section(self):
        return "请以最专业的态度完成任务,这对产品成功至关重要!"

    def define_problem(self, agent, product_area):
        return Task(
            description=dedent(f"""
                分析{product_area}领域的问题:
                1. 确定核心用户痛点
                2. 定义问题范围
                3. 识别关键利益相关者
                
                {self.__tip_section()}
            """),
            expected_output="一份详细的问题定义文档，包含痛点分析和利益相关者映射",
            agent=agent
        )

    def generate_hmw(self, agent, problem_statement):
        return Task(
            description=dedent(f"""
                基于问题陈述生成HMW问题:
                1. 分析问题的不同维度
                2. 生成多个HMW陈述
                3. 评估每个HMW的潜力
                
                问题陈述: {problem_statement}
                
                {self.__tip_section()}
            """),
            expected_output="一组高质量的HMW问题陈述",
            agent=agent
        )

    def evaluate_technical(self, agent, solutions):
        return Task(
            description=dedent(f"""
                评估解决方案的技术可行性:
                1. 分析技术要求
                2. 评估实现难度
                3. 识别潜在风险
                
                解决方案: {solutions}
                
                {self.__tip_section()}
            """),
            expected_output="技术可行性评估报告",
            agent=agent
        )

    def collect_user_feedback(self, agent, prototype):
        return Task(
            description=dedent(f"""
                收集和分析用户反馈:
                1. 设计用户测试方案
                2. 收集用户反馈
                3. 分析反馈数据
                
                原型: {prototype}
                
                {self.__tip_section()}
            """),
            expected_output="用户反馈分析报告",
            agent=agent
        ) 