# Scrapy Used Camera

## Getting Started

### Prerequisites

* Python 3.6.5
* Scrapy 1.6
* Splash 3.3.1
* Docker Engine 18.09.2
* MySQL 5.7

```
cd workspace
git clone https://github.com/Lara-Bell/scrapy-used-camera.git
```

### Installing

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Docker

```
# Splash And MySQL
docker-compose up -d

# Splash Only
docker-compose up -d splash
```

### Let's Start

```
cd app
scrapy crawl kitamura_used_spider
# OR
scrapy crawl mapcamera_used_spider
```

## Authors

- [Lara-Bell](https://github.com/Lara-Bell)

See also the list of [contributors](https://github.com/Lara-Bell/scrapy-used-camera/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
