serve:
	zola serve

dserve:
	zola serve --drafts

check:
	zola check

build:
	zola build

# pnpm install wrangler --save-dev
deploy:
	pnpm exec wrangler pages deploy public --project-name website-tabi --commit-dirty=true

publish:
	make build
	make deploy
