from crewai import Agent
from textwrap import dedent
from openai import OpenAI
from decouple import config
from langchain_community.chat_models import ChatOpenAI

class DesignAgents:
    def __init__(self):
        # 从环境变量获取配置
        self.api_key = config("OPENAI_API_KEY")
        self.base_url = config("OPENAI_BASE_URL")
        self.model_name = config("MODEL_NAME")
        
        # 配置 DeepSeek 客户端
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
        
        # 创建 LangChain 聊天模型
        self.llm = ChatOpenAI(
            client=self.client,
            model_name=self.model_name,
            temperature=0.7
        )

    def product_manager(self):
        return Agent(
            role="产品经理",
            backstory="""我是一名经验丰富的产品经理，专注于用户需求分析和产品战略制定。
                        我善于将业务目标转化为可执行的产品计划。""",
            goal="""定义产品愿景和目标，制定HMW陈述，设定设计约束，评估业务可行性""",
            verbose=True,
            llm=self.llm
        )

    def design_strategist(self):
        return Agent(
            role="设计策略师",
            backstory=dedent("""我是一名设计策略师，专注于用户体验和设计思维方法。
                            我善于通过设计思维来解决复杂问题。"""),
            goal=dedent("""负责用户研究分析，设计思维引导，原型设计建议，可用性测试设计"""),
            verbose=True,
            llm=self.llm
        )

    def technical_advisor(self):
        return Agent(
            role="技术顾问",
            backstory=dedent("""我是一名技术顾问，负责评估解决方案的技术可行性。
                            我有丰富的系统架构和技术选型经验。"""),
            goal=dedent("""进行技术可行性分析，提供架构建议，评估实现难度，识别技术风险"""),
            verbose=True,
            llm=self.llm
        )

    def user_advocate(self):
        return Agent(
            role="用户代言人",
            backstory=dedent("""我是用户代言人，深入理解用户需求和痛点。
                            我确保产品设计始终以用户为中心。"""),
            goal=dedent("""表达用户需求，收集用户反馈，评估用户体验，构建用户场景"""),
            verbose=True,
            llm=self.llm
        ) 