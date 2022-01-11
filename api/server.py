import os
from dotenv import load_dotenv
load_dotenv()

import uvicorn
from app import app

PORT=os.getenv('API_PORT', 5852)

if __name__ == "__main__":
    uvicorn.run(
        "server:app", 
        host="0.0.0.0", 
        port=int(PORT), 
        reload=True,
        workers=3,
        limit_max_requests=5)