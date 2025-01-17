# 使用node镜像构建前端
FROM node:18 as web-stage
WORKDIR /web
COPY ./web/package*.json .
RUN npm install
COPY ./web .
RUN npm run build


# 使用python镜像构建后端
FROM python:3.10 as server-stage
WORKDIR /server
COPY ./server/requirements.txt ./
RUN pip install -r requirements.txt
COPY ./server .

# 使用nginx镜像部署
FROM python:1.19.0-alpine as production-stage
RUN apt-get update
RUN apt-get install nginx
COPY --from=web-stage /web/dist /usr/share/nginx/html
COPY --from=server-stage /server /usr/share/nginx/html/backend
COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN ["python", "/usr/share/nginx/html/backend/start.py"]
