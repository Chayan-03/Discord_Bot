
# 🤖 Contest Notifier Discord Bot

A Python-based Discord bot that fetches and displays upcoming competitive programming contests from [clist.by](https://clist.by), including time conversion to IST.

---

## 🧠 Features

- Fetches contests from platforms like Codeforces, LeetCode, AtCoder, etc.
- Formats and converts contest start/end time to Indian Standard Time (IST).
- Displays contest duration.
- Fully asynchronous and uses environment variables for secure configuration.

---

## 🚧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Discord_Bot.git
cd Discord_Bot
```

---

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If no `requirements.txt` is present:
```bash
pip install discord.py aiohttp python-dotenv pytz
```

---

### 4. Create a `.env` File

In the root of the project directory, create a file named `.env` and add:

```
DISCORD_TOKEN=your_discord_bot_token
CLIST_API_KEY=username:api_key_from_clist
```

---

## 🔑 How to Get API Keys

### ▶️ Clist.by API Key

1. Go to [https://clist.by/accounts/login/](https://clist.by/accounts/login/)
2. Sign up or log in
3. Navigate to your profile > **API** tab: [https://clist.by/api/v2/doc/](https://clist.by/api/v2/doc/)
4. Copy the `username` and `api_key`
5. Add them as:
   ```
   CLIST_API_KEY=username:api_key
   ```

---

### 🤖 Set Up Your Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"**
3. Give your bot a name
4. Go to **Bot** tab → Click **"Add Bot"**
5. Copy the token → Add to `.env` as:
   ```
   DISCORD_TOKEN=your_token_here
   ```
6. Enable **Message Content Intent** under **Privileged Gateway Intents**
7. Go to **OAuth2 > URL Generator**:
   - Scopes: `bot`
   - Bot Permissions: `Send Messages`, `Embed Links`
   - Copy the URL and invite the bot to your server

---

## ▶️ Running the Bot

```bash
python bot.py
```

---

## ☁️ Deploying on EC2 / Linux Server

### 1. Install dependencies and activate environment
```bash
sudo apt update
sudo apt install python3.12 python3.12-venv git tmux
git clone https://github.com/your-username/Discord_Bot.git
cd Discord_Bot
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run bot in background using `tmux`
```bash
tmux
python bot.py
# Press Ctrl + B, then D to detach
```

To reattach:
```bash
tmux attach
```

---

## 📊 Monitoring EC2 Resources

```bash
htop       # CPU & RAM usage
df -h      # Disk usage
free -m    # RAM summary
top        # Live process monitor
```

---



---


