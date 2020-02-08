# use official Node.JS image
FROM node:8-jessie

# app's working directory
WORKDIR /usr/src/app

# install dependencies
COPY package.json .
RUN npm install

# inform that we will listen to port 80 (default port)
EXPOSE 80

# add source code
COPY . .

# command to start the app
CMD ["npm", "start"]