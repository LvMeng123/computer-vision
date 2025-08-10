import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 阶段定义
stages = {
    "Week 1": ["Tensor Ops", "Conv Basics", "Activation", "Pooling", "Mini-CNN Train Loop"],
    "Week 2-4": ["ResNet/MobileNet", "Advanced CNN", "Vision Transformer", "Data Augmentations", "Transfer Learning"],
    "Week 5-7": ["GAN", "Diffusion Models", "VAE", "Image-to-Image", "Text-to-Image"],
    "Week 8-10": ["Transformer for NLP", "BERT/GPT Fine-tune", "Prompt Engineering", "LoRA/PEFT"],
    "Week 11-12": ["CLIP", "BLIP-2", "Multi-modal Fusion", "LLM Agents", "RAG Pipelines"]
}

# 节点位置
positions = {
    "Week 1": (0, 0),
    "Week 2-4": (2, -1),
    "Week 5-7": (4, 0),
    "Week 8-10": (6, -1),
    "Week 11-12": (8, 0)
}

# 创建图
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('off')

# 绘制阶段框和文字
for stage, pos in positions.items():
    ax.add_patch(mpatches.FancyBboxPatch(
        (pos[0], pos[1]), 1.8, 1.2,
        boxstyle="round,pad=0.1",
        edgecolor="black", facecolor="#d4e6f1"
    ))
    ax.text(pos[0]+0.9, pos[1]+1.05, stage, ha='center', fontsize=12, fontweight='bold')
    
    # 绘制该阶段的技能点
    skills = stages[stage]
    for i, skill in enumerate(skills):
        ax.text(pos[0]+0.9, pos[1]+0.85 - i*0.18, f"- {skill}", fontsize=9, ha='center')

# 绘制连接箭头
arrowprops = dict(arrowstyle="->", color="gray", lw=1.5)
stage_keys = list(positions.keys())
for i in range(len(stage_keys)-1):
    start = positions[stage_keys[i]]
    end = positions[stage_keys[i+1]]
    ax.annotate("", xy=(end[0], end[1]+0.6), xytext=(start[0]+1.8, start[1]+0.6), arrowprops=arrowprops)

plt.tight_layout()
plt.show()
