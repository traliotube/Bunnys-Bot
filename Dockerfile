FROM --platform=arm64 python

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./Bunnys_Bot.py" ]