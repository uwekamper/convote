<script lang="ts">
    let {question} = $props()
    let my_text = question.text   // local copy of the question text

    let show_editor = $state(false)

    const saveEditor = () => {
      question.text = $state.snapshot(my_text)
      show_editor = false
    }
    
    const discardEditor = () => {
      my_text = question.text
      show_editor = false
    }
</script>

<div class="snes-container" style="margin-top: 20px; text-align: left; width: 50vw;">
  {#if show_editor}
  <div class="snes-form-group">
    <label for="input-question">Question</label>
    <div class="snes-input">
      <input id="input-question" type="text" value={my_text} onkeyup={(ev) => {my_text = ev.target.value}} placeholder="Enter a question" />
    </div>
  </div>

  <button class="snes-button" style="margin-right: 20px;" onclick={() => saveEditor()}>Save</button>
  <button class="snes-button has-plumber-color" onclick={() => discardEditor()}>Discard</button>
  {:else}
  <h4 class="snes-container-title has-ember-underline">{question.text}</h4>
  <div class="snes-form-group">
    <label>Answers</label>
    <div class="snes-radio snes-radio--vertical has-ember-icons">
      {#each question.answers as answer, index }
      <label class="snes-radio__item">
        <input type="radio" name="class" value="warrior" checked={index == 0} />
        <span class="snes-radio__item__content">{answer}</span>
      </label>
      {:else}
      No answers defined.
      {/each}
    </div>
  </div>
  <div>
  <a href="#" class="snes-link text-galaxy-color">Ask</a>
  <a href="#" class="snes-link text-plumber-color" onclick={() => { show_editor = true }}>Edit</a>
  </div>
  {/if}
</div>