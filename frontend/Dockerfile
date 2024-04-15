FROM node:21 as base

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm ci
COPY . ./

EXPOSE 5173


FROM base as dev

ENV NODE_ENV development

CMD ["npm", "run", "dev", "--", "--host"]

FROM base as prod

ENV NODE_ENV production
RUN npm run build

CMD ["node", "build"]