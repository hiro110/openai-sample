
# Quick Start

環境変数設定  
```
cp var.env.example var.env
vi var.env
```

Dokcer起動し、スクリプト実行  
```
docker-compose build
docker-compose up -d
docker-compose exec app bash
python startup.py
```

# Reference
https://python.langchain.com/en/latest/modules/models/llms/integrations/azure_openai_example.html
