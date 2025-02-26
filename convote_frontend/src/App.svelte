<script lang="ts">
  import 'snes.css/dist/snes.min.css'
  import { onMount } from 'svelte';
  import {Question} from './lib/Question.svelte.ts'
  import QuestionDisplay from './lib/QuestionDisplay.svelte'

  let questions = $state([])
  let is_loading = $state(true)
  let { endpoint: str } = $props();

  const addQuestion = () => {
    // let tmp_questions = $state.snapshot(questions)
    questions.push(new Question("What", []))
    
    // questions = tmp_questions
  }

  const removeQuestion = (index: number) => {
    // let tmp_questions = $state.snapshot(questions)
    //questions.push(new Question())
    questions.splice(index, 1);
    // questions = tmp_questions
  }

  /**
   * Lood questions on bootup 
   */
  onMount(async () => {
    const response = await fetch(`${endpoint}questions/`);
    const data = await response.json();
    console.log(data)
    for (let entry of data) {
      questions.push(new Question(entry.q, Object.values(entry.opts)))
    }
    is_loading = false;
  });
</script>

<main>

  <h1>convote</h1>
  {#if is_loading}
    <div>Loading questions from {endpoint}...</div>
  {:else}
    {#each questions as q, index}
    <QuestionDisplay question={q} index={index} />
    <div style="width: 98%; text-align: right; margin-top: -60px;">
      <button class="snes-button has-plumber-color" 
              title="Add another question" onclick={() => {removeQuestion(index)}}>-</button>
    </div>
    {/each}
  {/if}
  <div style="width: 100%; text-align: right; margin-top: 50px;">
    <button class="snes-button has-ocean-color" 
            title="Add another question" onclick={() => {addQuestion()}}>+</button>
            Add question
  </div>

</main>

<style>


</style>
