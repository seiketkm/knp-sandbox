FROM seiketkm/knp:v4.20-v2rc3
RUN apt-get update && \
    apt-get install -y \
    python3.8 \
    python3-pip && \
    apt-get clean
RUN pip3 install pipenv

RUN set -ex && mkdir /app
WORKDIR /app

ENV LC_ALL=C.UTF-8

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system
COPY . /app

ENV PORT '80'
EXPOSE 80
ENTRYPOINT ["python3", "app.py"] 
