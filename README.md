# Kanojo server

Barcode Kanojo server.

## Requirements:
- Python 3
- MongoDB

## Setup

- **Recommended** Install [virtualenv](https://virtualenv.pypa.io/en/latest/)
	- Recommended to be setup under `./venv/` directory.
	- Can also be installed from pip.
- Install python requirements from "requirements.txt"
```sh
python(3) -m pip -r requirements.txt
```
- Rename "config.py.template" to "config.py" and fill app parameters.

## Usage

 Now you can run server by:
`python(3) web_job.py`

## Docker
 If you prefer to run in docker, you can run it with:
```sh
docker run -it -d \
	-e PORT_VAL=5000 \
	-e HTTPS=False \
	-e MONGO_USERNAME=example \
	-e MONGO_PASSWORD=example \
	-e MONGO_HOST=example \
	-e MONGO_PORT=example \
	--name barcodekanojo \
	wegotshrimp/barcodekanojo 
```
 You will need to provide the information for the connection to the MongoDB server. If you wish to run the DB as a docker container, see Docker/docker_compose.yml for an example on how to do this with docker-compose.
 See https://hub.docker.com/r/wegotshrimp/barcodekanojo for more info on the environment variables you can set to control configuration.
## Licensing

Kanojo_server is licensed under MIT License Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
