<script lang="ts">
  import {counter} from "./CounterState.svelte.ts"
</script>
  
  
<button class="snes-button has-ember-color" onclick={() => {counter.reset()}}>
   Reset
</button>