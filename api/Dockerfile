FROM python:3.9-slim-buster

ENV PATH=/home/apps/bin:/home/apps/.local/bin:$PATH \
  LANG=en_US.UTF-8 \
  LANGUAGE=en_US:en \
  LC_ALL=en_US.UTF-8

COPY . /home/apps/api

RUN useradd --user-group --create-home apps
RUN chown -v -R apps:apps /home/apps

USER apps
WORKDIR /home/apps/api

RUN pip install --upgrade pip --user
RUN pip install --user --use-feature=in-tree-build /home/apps/api

ENTRYPOINT []
CMD ["uvicorn", "fastpypi.main:api", "--host", "0.0.0.0", "--port", "8000", "--log-config", "logging.yaml"]