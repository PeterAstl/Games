import random


def diamond():
    global money
    money *= 2


# # ["❌", "🍋", "🍒", "🍎", "🍊", "🍉", "🍔", "💎"]
items = {
"❌" : - 3,
"🍋" : + 1,
"🍒" : + 1,
"🍉" : + 2,
"🍔" : + 3,
"💎" : diamond,

}

def slot():
    global gamba
    for x in gamba:
        print(x)

playing = True
playcount = 3
score = -90
gambeling = True
money_emoji = ""
fruit_type = ""
starting_money = int(score / -playcount)

while playing:
    if playcount > 0:
        print(f"You got {playcount} tries left:")
        money = starting_money
        while gambeling:
            money_emoji = "🪙" * money
            print("\n" + str(money) + money_emoji)
            score += 1
            money -= 1
            if input("Would you like to cash out? (y): \n") != "y":

                spalten = 3
                reihen = 3
                goal = 3
                gamba = [[random.choice(list(items.keys())) for _ in range(spalten)] for _ in range(reihen)]

                if money > 0:
                    slot()

                    #  Diagonaler Hit
                    for r in range(reihen):
                        for s in range(spalten):
                            hit_count = 1
                            reihen_index = r
                            spalten_index = s

                            last_fruit = gamba[reihen_index][spalten_index]

                            while (reihen_index + 1 < reihen) and (spalten_index + 1 < spalten):
                                reihen_index += 1
                                spalten_index += 1

                                current_fruit = gamba[reihen_index][spalten_index]

                                if current_fruit == last_fruit:
                                    hit_count += 1
                                    if hit_count >= goal:
                                        print(f"↘️ Diagonaler Hit von ({r + 1}, {s + 1}) mit {hit_count}x {current_fruit}")
                                        fruit_type = current_fruit
                                        reward = items[current_fruit]
                                        if callable(reward):
                                            reward()
                                        else:
                                            money += reward

                                else:
                                    break

                    # Reihenhit
                    for row_index in range(len(gamba)):
                        row_hit = True
                        for item_index in range(len(gamba[row_index]) - 1):
                            if gamba[row_index][item_index] != gamba[row_index][item_index + 1] and row_hit:
                                row_hit = False
                        if row_hit:
                            fruit_type = gamba[row_index][0]
                            print(f"🎉 Treffer in ➡️ Reihe {row_index + 1} mit {fruit_type}!🎉")
                            reward = items[fruit_type]
                            if callable(reward):
                                reward()
                            else:
                                money += reward

                    #Spaltenhit
                    for column_index in range(len(gamba[0])):
                        column_hit = True
                        for item_index in range(len(gamba) - 1):
                            if gamba[item_index][column_index] != gamba[item_index + 1][column_index]:
                                column_hit = False
                        if column_hit:
                            fruit_type = gamba[0][column_index]
                            print(f"🎉 Treffer in ⬇️ Spalte {column_index + 1} mit {fruit_type}!🎉")
                            reward = items[fruit_type]
                            if callable(reward):
                                reward()
                            else:
                                money += reward

                else:
                    playcount -= 1
                    break


            else:
                playcount -= 1
                score += money
                break

    else:
        playing = False
        print("GAME OVER" + "\n")
        print("Your Score: " + (str(score)))