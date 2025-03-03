from datetime import datetime

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
                "舒适": ["宽敞", "温暖", "舒服", "自在"],
                "压抑": ["狭小", "封闭", "压抑", "闷"],
                "开放": ["开阔", "通透", "自由", "开放"],
                "局促": ["拥挤", "局促", "受限", "束缚"]
            },
            "时间": {
                "充裕": ["从容", "悠闲", "富余", "宽裕"],
                "紧张": ["赶", "忙", "急", "来不及"],
                "规律": ["有序", "计划", "按时", "规律"],
                "混乱": ["乱", "无序", "拖延", "混乱"]
            },
            "任务": {
                "专注": ["投入", "专心", "集中", "专注"],
                "分散": ["分心", "走神", "注意力分散"],
                "有序": ["条理", "步骤", "安排", "有序"],
                "混乱": ["杂乱", "无章", "混乱", "乱"]
            },
            "人际": {
                "亲密": ["亲近", "温暖", "信任", "亲密"],
                "疏离": ["疏远", "冷淡", "距离", "陌生"],
                "和谐": ["融洽", "友好", "和睦", "和谐"],
                "冲突": ["矛盾", "对立", "争执", "冲突"]
            }
        }

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
                    "强度": min(max_matches / 2, 1.0)
                }
        
        analysis_result["分析时间"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return analysis_result

    def generate_advice(self, emotion_analysis: dict) -> list:
        """生成情绪调节建议"""
        advice_list = []
        
        for dimension, analysis in emotion_analysis.items():
            if dimension == "分析时间":
                continue
                
            if analysis["状态"] == "未明确":
                continue
                
            if dimension == "空间":
                if analysis["状态"] in ["压抑", "局促"]:
                    advice_list.extend([
                        "空间调节：尝试重新布置您的环境，创造更开放的空间感",
                        "户外活动：每天安排一定时间到户外开放空间活动",
                        "采光改善：增加自然光照，使用明亮的色调装饰"
                    ])
                elif analysis["状态"] in ["舒适", "开放"]:
                    advice_list.append("空间维持：继续保持当前的空间布局，适时增添一些令人愉悦的装饰")
                    
            elif dimension == "时间":
                if analysis["状态"] in ["紧张", "混乱"]:
                    advice_list.extend([
                        "时间管理：使用番茄工作法，将任务分解为25分钟的专注时段",
                        "优先级：列出任务清单，按重要性和紧急性排序",
                        "缓冲时间：在规划时预留适当的缓冲时间，避免过度紧张"
                    ])
                elif analysis["状态"] in ["充裕", "规律"]:
                    advice_list.append("时间规划：保持当前的时间管理方式，适当记录成功经验")
                    
            elif dimension == "任务":
                if analysis["状态"] in ["分散", "混乱"]:
                    advice_list.extend([
                        "任务分解：将大任务分解为小目标，逐步完成",
                        "环境整理：清理工作环境，减少干扰因素",
                        "专注训练：使用专注力训练应用，培养专注习惯"
                    ])
                elif analysis["状态"] in ["专注", "有序"]:
                    advice_list.append("任务节奏：保持当前的工作节奏，适时奖励自己")
                    
            elif dimension == "人际":
                if analysis["状态"] in ["疏离", "冲突"]:
                    advice_list.extend([
                        "沟通改善：尝试开放式沟通，表达感受的同时也要倾听对方",
                        "边界设立：建立健康的人际边界，学会适度表达和拒绝",
                        "社交活动：参与适度的社交活动，培养新的社交关系"
                    ])
                elif analysis["状态"] in ["亲密", "和谐"]:
                    advice_list.append("关系维护：继续保持良好的人际关系，定期表达关心和感激")
        
        if not advice_list:
            advice_list = [
                "建议您多关注自己的情绪变化",
                "尝试记录每天的心情和感受",
                "如果需要，可以寻求专业的心理咨询支持"
            ]
        
        return advice_list

def main():
    coach = EmotionCoach()
    print("欢迎使用情绪教练！\n")
    print("请描述您当前的感受（比如：我最近感觉很压抑，工作总是赶不完，人际关系也很紧张）：")
    
    while True:
        user_input = input("\n您的输入（输入'退出'结束）：")
        if user_input == '退出':
            break
            
        # 分析情绪
        analysis = coach.analyze_emotion(user_input)
        print("\n=== 情绪分析结果 ===")
        for dimension, data in analysis.items():
            if dimension != "分析时间":
                print(f"\n{dimension}维度：")
                print(f"  状态：{data['状态'] or '未明确'}")
                print(f"  关键词：{', '.join(data['关键词']) if data['关键词'] else '无'}")
                print(f"  强度：{int(data['强度'] * 100)}%")
        
        # 生成建议
        advice = coach.generate_advice(analysis)
        print("\n=== 调节建议 ===")
        for i, suggestion in enumerate(advice, 1):
            print(f"{i}. {suggestion}")
        
        print("\n" + "="*50)

if __name__ == "__main__":
    main() 