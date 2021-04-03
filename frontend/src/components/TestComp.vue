<template>
<vue-resizable :width="200" :height="200" :min-height="200" :min-width="200" fit-parent drag-selector=".content" class="base">
    <div class="content"></div>
</vue-resizable>
</template>

<script>
import VueResizable from 'vue-resizable'
export default {
    name: "TestComp",
    components: {
        VueResizable
    }
}
</script>

<style scoped>
.content {
    background-color: burlywood;
    width: 100%;
    height: 100%;
    position: absolute;
}

.base {
    position: absolute;
}
</style>