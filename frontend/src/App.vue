<template>
  <div id="app">
    <div class="container">
      <theme-tile v-for="theme in themes" :theme="theme"></theme-tile>
      <topic-tile v-for="topic in topics" :topic="topic"></topic-tile>
    </div>
  </div>
</template>

<script>
import ThemeTile from "@/components/ThemeTile";
import TopicTile from '@/components/TopicTile';
export default {
  name: 'App',
  components: {
    ThemeTile,
    TopicTile
  },
  data: function() {
    return {
      themes: [
        {"id": 1, "title": "Internet", "left": 500, "top": 100},
        {"id": 2, "title": "Basic Frontend Knowledge", "left": 520, "top": 200},
        {"id": 3, "title": "OS and Genereal Knowledge", "left": 550, "top": 300}
      ],
      topics: [
        {"id": 1, "title": "How does the internet work?", "theme": 1, "left": 200, "top": 50},
        {"id": 2, "title": "What is HTTP?", "theme": 1, "left": 200, "top": 120},
        {"id": 3, "title": "Browsers and how they work?", "theme": 1, "left": 200, "top": 170},
        {"id": 4, "title": "DNS and how it works?", "theme": 1, "left": 800, "top": 50},
        {"id": 5, "title": "What is Domain Name?", "theme": 1, "left": 800, "top": 120},
        {"id": 6, "title": "What is hosting?", "theme": 1, "left": 800, "top": 170},
        {"id": 7, "title": "HTML", "theme": 2, "left": 200, "top": 230},
        {"id": 8, "title": "CSS", "theme": 2, "left": 800, "top": 230},
        {"id": 9, "title": "JavaScript", "theme": 2, "left": 800, "top": 280},
        {"id": 10, "title": "Terminal Usage", "theme": 3, "left": 200, "top": 500},
        {"id": 11, "title": "How OSs work in General", "theme": 3, "left": 200, "top": 550},
        {"id": 12, "title": "Process Management", "theme": 3, "left": 200, "top": 600},
        {"id": 13, "title": "Threads and Concurrency", "theme": 3, "left": 200, "top": 650},
        {"id": 14, "title": "Basic Terminal Commands", "theme": 3, "left": 200, "top": 700},
        {"id": 15, "title": "Memory Management", "theme": 3, "left": 200, "top": 750},
        {"id": 16, "title": "Interprocess Communication", "theme": 3, "left": 200, "top": 800},
        {"id": 17, "title": "I/O Management", "theme": 3, "left": 200, "top": 850},
        {"id": 18, "title": "POSIX Basics", "theme": 3, "left": 200, "top": 900},
        {"id": 19, "title": "Basic Networking Concepts", "theme": 3, "left": 200, "top": 950}
      ]
    }
},
}
</script>

<style>
.container {
  width: 100%;
  height: 2000px;
  display: inline-block;
}
</style>
