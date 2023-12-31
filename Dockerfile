# Dockerfile

# 此映像檔繼承安裝好 python:3.10 的 Linux 環境
FROM python:3.10

# 設定工作目錄
WORKDIR /code

# 複製 requirements 到工作目錄，下一步將會安裝相依的套件
# 由於這個檔案不經常更改，Docker 會檢測它並在這一步使用快取，也為下一步啟用快取
COPY ./requirements.txt /code/requirements.txt

# 執行 pip 命令安裝依賴項
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 複製專案程式碼到工作目錄
COPY ./src /code/src

COPY ./alembic.ini /code/alembic.ini
COPY ./alembic /code/alembic

# 設定啟動容器時要執行的指令
CMD alembic upgrade head;uvicorn src.main:app --host 0.0.0.0 --port 8000