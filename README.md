# Smart Lecture Repository

An AI-powered assistant for students to store lectures and get instant answers based on their content.

## Demo

![Login Screen](screenshots/Login%20Screen.jpg)
![Chat Interface](screenshots/Chat%20Interface.jpg)

## Product Context

- **End users:** Students of Innopolis University.
- **Problem:** Students often struggle to find specific information in long lecture notes or slides during exam preparation.
- **Solution:** A centralized repository where AI "reads" the lectures and answers questions using only the provided context.

## Features

- [x] Multi-format support (PDF, DOCX, TXT, PPTX)
- [x] Context-aware AI chat (gpt-oss-120b via OpenRouter)
- [x] User-specific lecture storage
- [ ] Support for image-based PDF (OCR) - *Future feature*

## Usage

1. Enter your nickname to login.
2. Upload a lecture file using the sidebar.
3. Select the lecture from the dropdown list.
4. Ask any question in the chat.

## Deployment

- **OS:** Ubuntu 24.04 (or any Linux with Docker support)
- **Requirements:** Docker, Docker Compose
- **Steps:**
  1. Clone the repo: `git clone https://github.com/MuS0rKa/se-toolkit-hackathon`
  2. Create a `.env` file with your `OPENROUTER_API_KEY`.
  3. Run `docker-compose up -d --build`.
  4. Open `http://10.93.26.31:8501` in your browser.
