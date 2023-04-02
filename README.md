<!-- Please be careful editing the below HTML, as GitHub is quite finicky with anything that looks like an HTML tag in GitHub Flavored Markdown. -->
# Linebot Template
<p align="center">
    <!-- Banner Placeholder -->
</p>
<p align="center">
  <b>建立基礎模板，提供二次開發</b>
</p>
<p align="center">
  <a href="https://github.com/Ron-Chang/linebot-template/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Ron-Chang/linebot-template" alt="License Badge">
  </a>
  <!--
      <a href="https://github.com/Ron-Chang/linebot-template/blob/main/CHANGELOG">
        <img src="https://img.shields.io/badge/view-changelog-green.svg" alt="Changelog Badge">
      </a>
  -->
</p>

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
