# Deploying this concept to Vercel

This ZIP has `index.html`, `vercel.json`, `assets/` and `api/` at its root. Extract the ZIP before deploying. The `api/products.py` file is a Vercel Python Function that reads current public product data from the official Les Miss Shopify store. If Shopify cannot be reached, the page displays a link to the official shop instead of inventing products.

## Deploy using Git

1. Extract the ZIP and create a Git repository containing the extracted files. Ensure `index.html` and `vercel.json` are at the repository root—not inside an extra folder.
2. Push that repository to GitHub, GitLab or Bitbucket and import it in Vercel.
3. Set **Root Directory** to the directory containing `index.html`, `api/` and `vercel.json`; if these files are at the repo root, leave it as `./`.
4. Choose **Other** as Framework Preset. Do not specify a build command or output directory. Deploy.
5. Open the deployment's root URL and visit `/api/products` to verify the API returns JSON. Confirm assets and shopping links load in your browser.

Alternatively, install the Vercel CLI, log in, `cd` into the extracted directory containing `vercel.json`, and run `vercel` (or `vercel --prod` for production). Follow the prompts. Ensure Vercel project settings do not override the root/output directory with settings from a previous project.

This is still an independent design prototype, **not a production-ready Shopify theme**. The Charm Builder, product details, account, cart, checkout and booking link to the existing official site; they are not integrated into this frontend. Authorized theme access, asset permission and thorough end-to-end validation are required for a live store. No actual Vercel deployment or checkout transaction was performed by the assistant.
