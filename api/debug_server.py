import os
from dotenv import load_dotenv
load_dotenv()

import uvicorn
from app import app

PORT=os.getenv('API_PORT', 5857)

if __name__ == "__main__":
    uvicorn.run(
        "debug_server:app", 
        host="0.0.0.0", 
        port=int(PORT), 
        reload=True, 
        log_level="info")