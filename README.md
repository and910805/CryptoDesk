<img width="467" height="288" alt="image" src="https://github.com/user-attachments/assets/f3c26e5b-29f7-4754-890e-7503f05180aa" />

# 📊 Data Monitor Widget

一個簡單的桌面浮動小工具，利用 **Python + Tkinter** 製作，  
可以即時顯示 **加密貨幣 / 股票** 的最新價格。  
支援多個交易所資料來源（Binance、MEXC、CoinGecko），  
股票則透過 Yahoo Finance 取得。

---

## ✨ 功能特色
- 💹 即時更新幣價與股價（預設每 5 秒更新一次）
- 📈 支援多個交易所：
  - Binance
  - MEXC
  - CoinGecko
- 📊 股票價格來源：Yahoo Finance
- 🖥️ Tkinter 視窗化：可拖曳、透明、永遠置頂
- ⚙️ 使用 `config.json` 自訂追蹤清單
- ⌨️ 熱鍵：`Esc` 可快速關閉程式

---

## 📂 專案結構
```

.
├── main.py         # 主程式，Tkinter widget
├── config.json     # 設定檔，定義要追蹤的幣種/股票

```

---

## ⚙️ 設定方式

### config.json 範例
```json
{
  "show_type": false,
  "crypto": [
    {"symbol": "BTCUSDT", "alias": "SYS01", "exchange": "binance"},
    {"symbol": "ETHUSDT", "alias": "SYS02", "exchange": "binance"},
    {"symbol": "SOLUSDT", "alias": "SYS03", "exchange": "binance"},
    {"symbol": "ADAUSDT", "alias": "SYS04", "exchange": "binance"},
    {"symbol": "MYXUSDT", "alias": "SYS05", "exchange": "mexc"}
  ]
}
```

* `show_type`: 是否顯示前綴 (`Crypto` / `Stock`)
* `symbol`: 幣種或股票代號
* `alias`: 顯示名稱（自訂）
* `exchange`: `binance` / `mexc` / `coingecko`

---

## 🚀 使用方式

1. 下載專案

   ```bash
   git clone https://github.com/<yourname>/data-monitor-widget.git
   cd data-monitor-widget
   ```

2. 安裝相依套件

   ```bash
   pip install -r requirements.txt
   ```

   或手動安裝：

   ```bash
   pip install requests yfinance screeninfo
   ```

3. 執行

   ```bash
   python main.py
   ```

4. 在桌面會看到一個浮動的視窗，顯示即時價格。
<img width="307" height="262" alt="image" src="https://github.com/user-attachments/assets/df925375-de68-4234-af32-50b3a2aca1e3" />

---

## 📦 相依套件

* `requests`
* `yfinance`
* `screeninfo`
* `tkinter`（Python 內建）

---

## 📜 授權

MIT License

---

## 📝 備註

* 預設每 5 秒更新一次資料，可自行在 `main.py` 裡調整 `self.root.after(5000, self.update_prices)`。
* 視窗可用滑鼠拖曳移動，適合放在副螢幕角落顯示。

要不要我順便幫你生一個 `requirements.txt`，讓別人可以直接 `pip install -r requirements.txt` 就能跑？
```
