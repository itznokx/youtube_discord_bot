FROM python:3.13

WORKDIR /usr/local/app
COPY . .
EXPOSE 6666 
RUN pip install --no-cache-dir -r bot_requeriments.txt 
RUN useradd app 
USER app 
CMD ["pwd"]
CMD ["ls","-a"]
CMD ["python3","./app/discord_bot.py"]
