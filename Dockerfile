FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 80

RUN ls

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]



