# ============================================================
#    配置文件 
# ============================================================

# ① 你的 API Key
#    智谱格式：{API Key ID}.{secret}
API_KEY = "5974cd7021bd45df979e3f0e233b595c.L25nLqBKVjvwYYsP"

# ② OpenAI 兼容 endpoint
#    智谱：https://open.bigmodel.cn/api/paas/v4
#    公司 Model Farm：https://YOUR_MODEL_FARM_ENDPOINT/openai/v1
BASE_URL = "https://open.bigmodel.cn/api/paas/v4"

# ③ 使用的模型
#    智谱免费可用：glm-4-flash（快）/ glm-4-air（质量更高）
#    公司 Model Farm：gemini-2.5-flash-lite / gpt-5-nano
MODEL = "glm-4-flash"

# ④ HTTP 代理（公司网络无法直连外网时填写，否则留空 ""）
#    格式示例：
#      "http://proxy.example.com:8080"
#      "http://username:password@proxy.example.com:8080"
#    若已设置系统环境变量 HTTPS_PROXY，此项可留空
PROXY = ""

# 服务监听地址
HOST = "0.0.0.0"
PORT = 8000

# 文件限制
MAX_FILE_SIZE_MB = 50
FILE_EXPIRE_HOURS = 24

# 本地临时目录（自动创建）
UPLOAD_DIR = "uploads"
RESULT_DIR = "results"

# 每张幻灯片最多一次发送的段落数（避免超出 context window）
BATCH_SIZE = 80
