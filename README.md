# SKU-Monitoring

SKU-Monitoring is a powerful application designed for businesses to effectively track and manage their SKU (Stock Keeping Unit) inventory. It provides real-time monitoring, analytics, and insights to help organizations streamline their supply chain, production schedules, and inventory management. The application offers features to track production cut-off dates, inventory levels, and other critical SKU-related metrics.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
6. [Contributing](#contributing)
7. [License](#license)

## Features

- **Real-Time Inventory Monitoring:** Keep track of inventory levels for each SKU and receive alerts for low stock or overstock situations.
- **Production Cut-Off Tracking:** Monitor and manage production cut-off dates to ensure timely scheduling and minimize delays.
- **SKU Analytics & Reporting:** Generate reports to gain insights into SKU performance, forecast trends, and optimize inventory.
- **Customizable Notifications:** Set up alerts for specific events, such as production deadlines or stock depletion.
- **Integration-Friendly API:** Integrates seamlessly with ERP systems, databases, and third-party applications.
- **User-Friendly Dashboard:** Visualize your SKU data in an intuitive and interactive dashboard.

## Installation

To install and run the SKU-Monitoring application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/skucaster/sku-monitoring.git
   ```
2. Navigate to the project directory:
   ```bash
   cd sku-monitoring
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the application:
   ```bash
   python app.py
   ```

## Usage

After installing, access the SKU-Monitoring dashboard by navigating to `http://localhost:5000` in your web browser.

1. **Upload SKU Data**: Use the dashboard's "Upload Data" feature to upload your inventory and SKU data.
2. **Set Alerts**: Navigate to the "Settings" section to configure alerts for production cut-off dates and stock levels.
3. **View Reports**: Use the "Reports" tab to generate custom reports on SKU performance and inventory trends.

## Configuration

SKU-Monitoring supports custom configurations through a `.env` file:

```ini
# .env file
DATABASE_URL=postgresql://user:password@localhost:5432/sku_db
ALERT_EMAIL=support@skucaster.com
THRESHOLD_LOW_STOCK=50
THRESHOLD_HIGH_STOCK=500
```

For advanced configuration options, see the [Configuration Guide](docs/configuration.md).


## Contributing

We welcome contributions to the SKU-Monitoring project! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.

## License

This project is licensed under the GLPv3 License - see the [LICENSE](LICENSE) file for details.

## Contact

For support or questions, please reach out to our team at [support@skucaster.com](mailto:support@skucaster.com).

