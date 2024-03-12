import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Hello World！",
  description: "Example vitepress site",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Java', link: '/java/list' },
      { text: 'Examples', link: '/example/markdown-examples' }
    ],

    sidebar: {
      '/example/': [
        {
          text: 'Examples',
          items: [
            { text: 'Markdown Examples', link: '/example/markdown-examples' },
            { text: 'Runtime API Examples', link: '/example/api-examples' }
          ]
        }
      ],
      '/java/': [
        {
          text: 'Java',
          items: [
            { text: '一览', link: '/java/list' }
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
