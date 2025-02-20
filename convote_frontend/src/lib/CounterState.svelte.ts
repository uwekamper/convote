
class CounterState {
    #count = $state(0)

    get count() {
        return this.#count
    }
    set count(v) {
        this.#count = v
    }
    reset = () => {
        this.#count = 0
    }
    increment = () => {
        this.#count += 1
    }
}

export const counter = new CounterState()
