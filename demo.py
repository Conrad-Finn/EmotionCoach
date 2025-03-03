from datetime import datetime
import time
import os

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class EmotionCoach:
    def __init__(self):
        self.emotion_flower = {
            "空间": ["舒适", "压抑", "开放", "局促"],
            "时间": ["充裕", "紧张", "规律", "混乱"],
            "任务": ["专注", "分散", "有序", "混乱"],
            "人际": ["亲密", "疏离", "和谐", "冲突"]
        }
        
        self.emotion_keywords = {
            "空间": {
                "舒适": ["宽敞", "温暖", "舒服", "自在", "安心"],
                "压抑": ["狭小", "封闭", "压抑", "闷", "局促"],
                "开放": ["开阔", "通透", "自由", "开放", "空旷"],
                "紧张": ["拥挤", "密集", "受限", "束缚", "挤"]
            },
            "时间": {
                "充裕": ["从容", "悠闲", "富余", "宽裕", "轻松"],
                "紧张": ["赶", "忙", "急", "来不及", "焦虑"],
                "规律": ["有序", "计划", "按时", "规律", "节奏"],
                "混乱": ["乱", "无序", "拖延", "混乱", "杂乱"]
            },
            "任务": {
                "专注": ["投入", "专心", "集中", "专注", "沉浸"],
                "分散": ["分心", "走神", "注意力分散", "杂念"],
                "有序": ["条理", "步骤", "安排", "有序", "明确"],
                "混乱": ["杂乱", "无章", "混乱", "乱", "困惑"]
            },
            "人际": {
                "亲密": ["亲近", "温暖", "信任", "亲密", "友好"],
                "疏离": ["疏远", "冷淡", "距离", "陌生", "孤独"],
                "和谐": ["融洽", "友好", "和睦", "和谐", "平和"],
                "冲突": ["矛盾", "对立", "争执", "冲突", "紧张"]
            }
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_welcome(self):
        self.clear_screen()
        print(f"{Colors.HEADER}{'='*60}")
        print(f"{Colors.BOLD}欢迎使用情绪教练 - EmotionCoach{Colors.ENDC}")
        print(f"您的贴心情绪分析助手")
        print(f"{Colors.HEADER}{'='*60}{Colors.ENDC}\n")

    def print_dimensions(self):
        print(f"\n{Colors.BLUE}我们关注的四个维度：{Colors.ENDC}")
        print(f"{Colors.YELLOW}✧ 空间维度：{Colors.ENDC}您所处的环境给您带来的感受")
        print(f"{Colors.YELLOW}✧ 时间维度：{Colors.ENDC}您对时间流逝的感知和规划")
        print(f"{Colors.YELLOW}✧ 任务维度：{Colors.ENDC}您在处理事务时的状态")
        print(f"{Colors.YELLOW}✧ 人际维度：{Colors.ENDC}您与他人互动的情况\n")

    def analyze_emotion(self, user_input: str) -> dict:
        """分析用户情绪状态"""
        analysis_result = {
            "空间": {"状态": None, "关键词": [], "强度": 0},
            "时间": {"状态": None, "关键词": [], "强度": 0},
            "任务": {"状态": None, "关键词": [], "强度": 0},
            "人际": {"状态": None, "关键词": [], "强度": 0}
        }
        
        for dimension, emotions in self.emotion_keywords.items():
            max_matches = 0
            best_emotion = None
            matched_keywords = []
            
            for emotion, keywords in emotions.items():
                matches = []
                for keyword in keywords:
                    if keyword in user_input:
                        matches.append(keyword)
                
                if len(matches) > max_matches:
                    max_matches = len(matches)
                    best_emotion = emotion
                    matched_keywords = matches
            
            if best_emotion:
                analysis_result[dimension] = {
                    "状态": best_emotion,
                    "关键词": matched_keywords,
                    "强度": min(max_matches / 3, 1.0)
                }
        
        analysis_result["分析时间"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return analysis_result

    def generate_advice(self, emotion_analysis: dict) -> list:
        """生成情绪调节建议"""
        advice_list = []
        
        for dimension, analysis in emotion_analysis.items():
            if dimension == "分析时间" or analysis["状态"] is None:
                continue
                
            if dimension == "空间":
                if analysis["状态"] in ["压抑", "紧张"]:
                    advice_list.extend([
                        f"{Colors.GREEN}✿ 空间调节：{Colors.ENDC}尝试重新布置您的环境，创造更开放的空间感",
                        f"{Colors.GREEN}✿ 户外活动：{Colors.ENDC}每天安排一定时间到户外开放空间活动",
                        f"{Colors.GREEN}✿ 采光改善：{Colors.ENDC}增加自然光照，使用明亮的色调装饰"
                    ])
                elif analysis["状态"] in ["舒适", "开放"]:
                    advice_list.append(f"{Colors.GREEN}✿ 空间维持：{Colors.ENDC}继续保持当前的空间布局，适时增添一些令人愉悦的装饰")
                    
            elif dimension == "时间":
                if analysis["状态"] in ["紧张", "混乱"]:
                    advice_list.extend([
                        f"{Colors.BLUE}❀ 时间管理：{Colors.ENDC}使用番茄工作法，将任务分解为25分钟的专注时段",
                        f"{Colors.BLUE}❀ 优先级：{Colors.ENDC}列出任务清单，按重要性和紧急性排序",
                        f"{Colors.BLUE}❀ 缓冲时间：{Colors.ENDC}在规划时预留适当的缓冲时间，避免过度紧张"
                    ])
                elif analysis["状态"] in ["充裕", "规律"]:
                    advice_list.append(f"{Colors.BLUE}❀ 时间规划：{Colors.ENDC}保持当前的时间管理方式，适当记录成功经验")
                    
            elif dimension == "任务":
                if analysis["状态"] in ["分散", "混乱"]:
                    advice_list.extend([
                        f"{Colors.YELLOW}❁ 任务分解：{Colors.ENDC}将大任务分解为小目标，逐步完成",
                        f"{Colors.YELLOW}❁ 环境整理：{Colors.ENDC}清理工作环境，减少干扰因素",
                        f"{Colors.YELLOW}❁ 专注训练：{Colors.ENDC}使用专注力训练应用，培养专注习惯"
                    ])
                elif analysis["状态"] in ["专注", "有序"]:
                    advice_list.append(f"{Colors.YELLOW}❁ 任务节奏：{Colors.ENDC}保持当前的工作节奏，适时奖励自己")
                    
            elif dimension == "人际":
                if analysis["状态"] in ["疏离", "冲突"]:
                    advice_list.extend([
                        f"{Colors.RED}❃ 沟通改善：{Colors.ENDC}尝试开放式沟通，表达感受的同时也要倾听对方",
                        f"{Colors.RED}❃ 边界设立：{Colors.ENDC}建立健康的人际边界，学会适度表达和拒绝",
                        f"{Colors.RED}❃ 社交活动：{Colors.ENDC}参与适度的社交活动，培养新的社交关系"
                    ])
                elif analysis["状态"] in ["亲密", "和谐"]:
                    advice_list.append(f"{Colors.RED}❃ 关系维护：{Colors.ENDC}继续保持良好的人际关系，定期表达关心和感激")
        
        if not advice_list:
            advice_list = [
                f"{Colors.BLUE}✧ 情绪觉察：{Colors.ENDC}建议您多关注自己的情绪变化",
                f"{Colors.BLUE}✧ 情绪记录：{Colors.ENDC}尝试记录每天的心情和感受",
                f"{Colors.BLUE}✧ 专业支持：{Colors.ENDC}如果需要，可以寻求专业的心理咨询支持"
            ]
        
        return advice_list

    def print_analysis(self, analysis: dict):
        print(f"\n{Colors.HEADER}=== 情绪分析结果 ==={Colors.ENDC}")
        for dimension, data in analysis.items():
            if dimension != "分析时间":
                if data["状态"]:
                    intensity = "●" * int(data["强度"] * 5) + "○" * (5 - int(data["强度"] * 5))
                    print(f"\n{Colors.YELLOW}{dimension}维度：{Colors.ENDC}")
                    print(f"  状态：{Colors.BOLD}{data['状态']}{Colors.ENDC}")
                    print(f"  关键词：{Colors.GREEN}{', '.join(data['关键词'])}{Colors.ENDC}")
                    print(f"  强度：{Colors.BLUE}{intensity}{Colors.ENDC} {int(data['强度'] * 100)}%")

    def print_advice(self, advice: list):
        print(f"\n{Colors.HEADER}=== 调节建议 ==={Colors.ENDC}")
        for suggestion in advice:
            print(f"\n{suggestion}")

def main():
    coach = EmotionCoach()
    coach.print_welcome()
    coach.print_dimensions()
    
    print(f"{Colors.GREEN}示例：我最近感觉很压抑，工作总是赶不完，人际关系也很紧张{Colors.ENDC}")
    print(f"\n{Colors.BOLD}请描述您当前的感受：{Colors.ENDC}")
    
    while True:
        user_input = input(f"\n{Colors.BLUE}您的输入{Colors.ENDC}（输入'退出'结束）：")
        if user_input.lower() in ['退出', 'exit', 'quit']:
            print(f"\n{Colors.GREEN}感谢使用情绪教练，愿您保持愉快的心情！{Colors.ENDC}")
            break
            
        # 分析情绪
        analysis = coach.analyze_emotion(user_input)
        coach.print_analysis(analysis)
        
        # 生成建议
        advice = coach.generate_advice(analysis)
        coach.print_advice(advice)
        
        print(f"\n{Colors.HEADER}{'='*60}{Colors.ENDC}")
        time.sleep(1)

if __name__ == "__main__":
    main() 