# Website Screenshot Crawler

A template for automated website screenshot capturing. This actor takes screenshots of websites from specified URLs, uploads them to Apify Key-Value Store, and provides screenshot URLs in a dataset. It is ideal for monitoring website changes, archiving web content, or capturing visuals for reports. The actor uses [Pyppeteer](https://pyppeteer.github.io/pyppeteer/) for browser automation and screenshot generation.

## Included Features

- **[Apify SDK](https://docs.apify.com/sdk/python/)** - A toolkit for building Apify Actors and scrapers in Python.
- **[Pyppeteer](https://pyppeteer.github.io/pyppeteer/)** - A Python port of Puppeteer, an open-source tool for automating web browsers using a high-level API.
- **[Key-Value Store](https://docs.apify.com/sdk/python/docs/concepts/storages#working-with-key-value-stores)** - Store screenshots and metadata for easy retrieval.
- **[Dataset](https://docs.apify.com/sdk/python/docs/concepts/storages#working-with-datasets)** - Structured storage for results like screenshot URLs and metadata.
- **Cookie and Viewport Support** - Allows setting cookies and specifying the viewport dimensions before capturing screenshots.

## Input

The input for this actor should be JSON containing the necessary configuration. The only required field is `link_urls`, which must be an array of website URLs. All other fields are optional. Here’s a detailed description of the input fields:

| Field                          | Type     | Description                                                                                          | Allowed Values                                   |
|--------------------------------|----------|------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `link_urls`                   | Array    | An array of website URLs to capture screenshots of.                                                | Any valid URL                                    |
| `Sleep`                       | Number   | Duration to wait after the page has loaded before taking a screenshot (in seconds).                 | Minimum: 0, Maximum: 3600                        |
| `waitUntil`                   | String   | Event to wait for before taking the screenshot.                                                    | One of: `"load"`, `"domcontentloaded"`, `"networkidle2"`, `"networkidle0"` |
| `cookies`                     | Array    | Any cookies to set for the browser session.                                                         | Array of cookie objects                          |
| `fullPage`                    | Boolean  | Whether to capture the full page or just the viewport.                                             | `true` or `false`                               |
| `window_Width`                | Number   | Width of the browser viewport.                                                                       | Minimum: 100, Maximum: 3840                      |
| `window_Height`               | Number   | Height of the browser viewport.                                                                      | Minimum: 100, Maximum: 2160                      |
| `scrollToBottom`              | Boolean  | Should the browser scroll to the bottom of the page before taking a screenshot?                     | `true` or `false`                               |
| `distance`                    | Number   | Distance (in pixels) to scroll down for each scroll action.                                         | Minimum: 0                                       |
| `delay`                       | Number   | Delay (in milliseconds) between scroll actions.                                                     | Minimum: 0, Maximum: 3600000                     |
| `delayAfterScrolling`         | Number   | Specify the delay (in milliseconds) after scrolling to the bottom of the page before taking a screenshot. | Minimum: 0, Maximum: 3600000                     |
| `waitUntilNetworkIdleAfterScroll` | Boolean | Choose whether to wait for the network to become idle after scrolling to the bottom of the page.   | `true` or `false`                               |
| `waitUntilNetworkIdleAfterScrollTimeout` | Number | Maximum wait time (in milliseconds) for the network to become idle after scrolling.                 | Minimum: 1000, Maximum: 3600000                  |

For more information about the `waitUntil` parameter, please refer to the [Puppeteer page.goto function documentation](https://pptr.dev/#?product=Puppeteer&version=v8.0.0&show=api-class-page).

## Output

Once the actor finishes executing, it will output a screenshot of each website into a file stored in the Key-Value Store associated with the run. The screenshot URLs will also be stored in a dataset for easy access.

## How It Works

1. **Input Configuration**: The actor reads the input data as specified above.
2. **Browser Automation**: The actor launches a headless browser using Pyppeteer, loading the target URLs, and capturing screenshots.
3. **Setting Cookies and Viewport**: Before navigating to each link, specified cookies are set using `page.setCookie()`, and the viewport is configured with specified width and height.
4. **Page Navigation**: The actor navigates to each URL using `page.goto()`, waiting for the specified `waitUntil` event.
5. **Scrolling (Optional)**: If the `scrollToBottom` option is enabled, the actor executes a scrolling script that scrolls down the page by the defined `distance` in pixels.
6. **Screenshot Capture**: After the page has fully loaded, the actor waits for the `Sleep` duration before capturing the screenshot and saves it with a random filename.
7. **Uploading Screenshots**: The captured screenshots are read as binary data and uploaded to the Apify Key-Value Store using `Actor.set_value()`, with URLs stored in the dataset.
8. **Logging and Error Handling**: The actor logs the success or failure of each URL processed, ensuring that it can continue processing even if one fails.
9. **Cleanup**: After processing all URLs, the actor closes the browser.

This open-source actor effectively automates the process of capturing and storing screenshots of multiple web pages, making it a valuable tool for monitoring website changes, archiving content, or generating visual reports.

## Resources

- [Pyppeteer Documentation](https://pyppeteer.github.io/pyppeteer/)
- [Apify Python SDK](https://docs.apify.com/sdk/python)
- [Apify Actors](https://apify.com/actors)
- [Automated Web Scraping Guide](https://docs.apify.com/academy/python)
- [Apify Forum](https://forum.apify.com/)

## Getting Started

To get started with this actor:

1. **Build the Actor**: Define your input URLs and configure optional settings like scrolling and sleep duration.
2. **Run the Actor**: Execute the actor on the Apify platform or locally using the Apify CLI.

## Pull the Actor for Local Development

To develop this actor locally, follow these steps:

1. Install `apify-cli`:

    **Using Homebrew**:

    ```bash
    brew install apify-cli
    ```

    **Using NPM**:

    ```bash
    npm install -g apify-cli
    ```

2. Pull the Actor using its unique `<ActorId>`:

    ```bash
    apify pull <ActorId>
    ```

## Example Use Cases

- **Website Monitoring**: Capture screenshots periodically to monitor changes to web pages.
- **Visual Archiving**: Store visual representations of websites over time for research or archival purposes.
- **Reporting**: Automatically capture visuals for reports or presentations.

## Documentation Reference

- [Apify SDK for Python](https://docs.apify.com/sdk/python)
- [Apify Platform Documentation](https://docs.apify.com/platform)
- [Pyppeteer API Documentation](https://pyppeteer.github.io/pyppeteer/)
- [Join the Apify Developer Community](https://discord.com/invite/jyEM2PRvMU)

## Contact Information

For any inquiries, you can reach me at:  
Email: [flowextractapi@outlook.com](mailto:flowextractapi@outlook.com)  
GitHub: [https://github.com/FlowExtractAPI](https://github.com/FlowExtractAPI)  
Twitter: [https://x.com/FlowExtractAPI](https://x.com/FlowExtractAPI)