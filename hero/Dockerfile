FROM node:8-alpine

COPY . /home/hero/

WORKDIR /home/hero/
RUN pwd
RUN ls -alh
RUN npm install
CMD ["npm", "run", "start"]
