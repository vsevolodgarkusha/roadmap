<template>
<vue-resizable
    :id="'main-theme'+theme.id"
    :left="theme.left"
    :top="theme.top"
    fit-parent
    drag-selector=".content"
    class="theme-tile"
    active=""
>
    <div class="content" :id="'theme'+theme.id">
        <input type="checkbox" class="checkbox">
        {{theme.title}}
    </div>
</vue-resizable>
</template>

<script>
import VueResizable from 'vue-resizable'
export default {
    name: "ThemeTile",
    props: ['theme'],
    components: {
        VueResizable,
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
    border-radius: 3px;
    border: 1px solid black;
    text-align: center;
    padding: 15px;
    background-color: rgb(255, 243, 68);
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    font-size: 15px;
}
.theme-tile {
    position: absolute;
}
.checkbox {
    position: absolute;
    left: -5px;
    top: -5px;
    border-radius: 50%;
}
</style>