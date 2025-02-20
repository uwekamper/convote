<script lang="ts">
  import {counter} from "./CounterState.svelte.ts"
</script>


<button class="snes-button has-plumber-color" onclick={() => {counter.increment()}}>
  count is {counter.count}
</button>