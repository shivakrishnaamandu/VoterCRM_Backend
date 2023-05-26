FROM python:3.9

COPY ./BackEnd/requirements.txt requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

COPY ./BackEnd /app/BackEnd
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["python"]
CMD ["/app/BackEnd/main.py"]