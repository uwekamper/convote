export class Question {
    #text = $state("Do you have a question?")
    #answers = $state(["Yes", "No"])

    get text() {
        return this.#text
    }

    set text(v) {
        this.#text = v
    }

    get answers() {
        return this.#answers
    }
    set answers(v) {
        this.#answers = v
    }
    // increment = () => {
    //    this.#count += 1
    // }
}
