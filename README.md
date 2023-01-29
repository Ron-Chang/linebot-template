# Linebot Template (Line 機器人模板)

## Goal 目的
- 建立基礎模板，提供二次開發

## Usage 使用方法
- 於[Line Developers](https://developers.line.biz/)申請開發者帳號
    1. Issue 取得 Channel secret
    2. Issue 取得 Channel access token
- 複製 .env.example 為 .env 並填入空項
    - `SECRET_KEY`: 任意字串
    - `APP_IMAGE`: 個人的倉庫地址
    - `STAGE`: 環境
    - 將取得的 _Channel secret_ 填入 `LINEBOT_SECRET`
    - 將取得的 _Channel access token_ 填入 `LINEBOT_ACCESS_TOKEN`
- 啟動專案
    1. `make build`
    2. `make uu`
    3. `docker compose logs -f`
