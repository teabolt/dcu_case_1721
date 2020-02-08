# use official node image
FROM node

# app working directory
WORKDIR /usr/bin/ddashweb

# copy and install dependencies
COPY package*.json /usr/bin/ddashweb/
RUN npm install

# make react app unmanaged
RUN npm install react-scripts -g

# bundle source code
COPY . .

# inform the port that we will be listening on
EXPOSE 8080

# set start command
CMD ["npm", "start"]