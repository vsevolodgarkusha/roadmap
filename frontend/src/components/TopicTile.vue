<template>
<vue-resizable
    :id="'main-topic'+topic.id"
    :left="topic.left"
    :top="topic.top"
    fit-parent
    drag-selector=".content"
    class="topic-tile"
    active=""
>
    <div class="content" :id="'topic'+topic.id">
        <input type="checkbox" class="checkbox">
        {{topic.title}}
    </div>
</vue-resizable>
</template>

<script>
import VueResizable from 'vue-resizable'
import Checkbox from 'vue-material-checkbox'

export default {
    name: "TopicTile",
    props: ['topic'],
    components: {
        VueResizable,
        Checkbox
    },
    mounted() {
        this.$children[0].w = parseInt(this.$el.style.width)
        this.$children[0].h = parseInt(this.$el.style.height)
    }
}
</script>

<style scoped>
.content {
    width: auto;
    height: auto;
    min-width: 100px;
    max-width: 200px;
    border-radius: 2px;
    border: 1px solid black;
    text-align: center;
    padding: 15px;
    background-color: rgb(222, 135, 135);
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    font-size: 15px;
}
.topic-tile {
    position: absolute;
}
.checkbox {
    position: absolute;
    left: -5px;
    top: -5px;
    border-radius: 50%;
}
</style>