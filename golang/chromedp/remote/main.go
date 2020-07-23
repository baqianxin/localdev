// Command remote is a chromedp example demonstrating how to connect to an
// existing Chrome DevTools instance using a remote WebSocket URL.
package main

import (
	"context"
	"flag"
	"fmt"
	"log"

	"github.com/chromedp/cdproto/network"
	"github.com/chromedp/chromedp"
)

var flagDevToolWsUrl = flag.String("devtools-ws-url", "ws://127.0.0.1:9222/devtools/page/641D8D9F3CAB30A96D3C9C8FC6DAC17B", "DevTools WebSocket URL")

func main() {
	// Create contexts.
	opts := append(chromedp.DefaultExecAllocatorOptions[:], chromedp.Flag("headless", false))
	actx, cancel := chromedp.NewExecAllocator(context.Background(), opts...)
	defer cancel()
	ctx, cancel := chromedp.NewContext(actx)

	// Call cancel() to close Chrome on some condition.
	if false {
		cancel()
	}

	// Custom header.
	headers := map[string]interface{}{
		"X-Header": "my request header",
	}
	var body string
	task := chromedp.Tasks{
		network.Enable(),
		network.SetExtraHTTPHeaders(network.Headers(headers)),
		chromedp.Navigate("https://duckduckgo.com"),
		chromedp.OuterHTML("html", &body),
	}
	defer cancel()
	// Run task.
	err := chromedp.Run(ctx, task)
	if err != nil {
		log.Fatal(err)
	}
	log.Println("Body of duckduckgo.com starts with:")
	log.Println(body[0:10])
}
func main2() {
	flag.Parse()
	fmt.Println(*flagDevToolWsUrl)
	if *flagDevToolWsUrl == "" {
		log.Fatal("must specify -devtools-ws-url")
	}

	// create allocator context for use with creating a browser context later
	allocatorContext, cancel := chromedp.NewRemoteAllocator(context.Background(), *flagDevToolWsUrl)
	defer cancel()

	// create context
	ctxt, cancel := chromedp.NewContext(allocatorContext)
	defer cancel()

	// run task list
	var body string
	if err := chromedp.Run(ctxt,
		chromedp.Navigate("https://duckduckgo.com"),
		chromedp.WaitVisible("#logo_homepage_link"),
		chromedp.OuterHTML("html", &body),
	); err != nil {
		log.Fatalf("Failed getting body of duckduckgo.com: %v", err)
	}

	log.Println("Body of duckduckgo.com starts with:")
	log.Println(body[0:10])
}
