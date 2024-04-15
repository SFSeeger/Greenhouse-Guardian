# ██████   █████  ███████ ███████ 
# ██   ██ ██   ██ ██      ██      
# ██████  ███████ ███████ █████   
# ██   ██ ██   ██      ██ ██      
# ██████  ██   ██ ███████ ███████ 
FROM node:21 as base

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm ci
COPY . ./


# ██████  ███████ ██    ██ 
# ██   ██ ██      ██    ██ 
# ██   ██ █████   ██    ██ 
# ██   ██ ██       ██  ██  
# ██████  ███████   ████   
FROM base as dev

ENV NODE_ENV development
EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]


# ██████  ██████   ██████  ██████  
# ██   ██ ██   ██ ██    ██ ██   ██ 
# ██████  ██████  ██    ██ ██   ██ 
# ██      ██   ██ ██    ██ ██   ██ 
# ██      ██   ██  ██████  ██████  
FROM base as prod

ENV NODE_ENV production
RUN npm run build

CMD ["node", "build"]