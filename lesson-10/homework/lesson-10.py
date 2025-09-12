1)from datetime import datetime
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date  # format: 'YYYY-MM-DD'
        self.completed = False
    def mark_completed(self):
        self.completed = True
    def __str__(self):
        status = "✅ Tugallangan" if self.completed else "❌ Tugallanmagan"
        return f"Nomi: {self.title}\nTavsif: {self.description}\nTugash sanasi: {self.due_date}\nHolati: {status}"
      class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
        print(f"✅ Vazifa qo'shildi: {task.title}")
    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"✅ '{self.tasks[index].title}' tugallandi.")
        else:
            print("❌ Noto‘g‘ri indeks!")
    def list_all_tasks(self):
        if not self.tasks:
            print("🚫 Hozircha hech qanday vazifa mavjud emas.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"\n#{i + 1}\n{task}")
    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if not task.completed]
        if not incomplete:
            print("🎉 Barcha vazifalar bajarilgan!")
        else:
            for i, task in enumerate(incomplete):
                print(f"\n#{i + 1}\n{task}")
              def main():
    todo = ToDoList()
    while True:
        print("\n=== ToDoList CLI ===")
        print("1. Vazifa qo'shish")
        print("2. Vazifani tugallangan deb belgilash")
        print("3. Barcha vazifalarni ko'rsatish")
        print("4. Tugallanmagan vazifalarni ko'rsatish")
        print("5. Chiqish")
        choice = input("Tanlang (1-5): ")
        if choice == '1':
            title = input("Vazifa nomi: ")
            description = input("Tavsifi: ")
            due_date = input("Tugash sanasi (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo.add_task(task)
        elif choice == '2':
            todo.list_all_tasks()
            try:
                idx = int(input("Qaysi vazifa tugallandi? Raqamini kiriting: ")) - 1
                todo.mark_task_completed(idx)
            except ValueError:
                print("❌ Raqam kiritilmadi!")
        elif choice == '3':
            todo.list_all_tasks()
        elif choice == '4':
            todo.list_incomplete_tasks()
        elif choice == '5':
            print("✅ Dasturni yakunlandi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov! 1-5 oralig‘ida tanlang.")
          if __name__ == "__main__":
    main()
=== ToDoList CLI ===
1. Vazifa qo'shish
2. Vazifani tugallangan deb belgilash
3. Barcha vazifalarni ko'rsatish
4. Tugallanmagan vazifalarni ko'rsatish
5. Chiqish
✅ Dasturni yakunlandi.

2)from datetime import datetime
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()
    def edit_content(self, new_content):
        self.content = new_content
        print(f"✏️ Post '{self.title}' tahrirlandi.")
    def __str__(self):
        return (f"Sarlavha: {self.title}\n"
                f"Muallif: {self.author}\n"
                f"Yaratilgan: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Kontent:\n{self.content}")
class Blog:
    def __init__(self):
        self.posts = []
    def add_post(self, post):
        self.posts.append(post)
        print(f"✅ Post qo'shildi: '{post.title}'")
    def list_all_posts(self):
        if not self.posts:
            print("🚫 Hozircha postlar mavjud emas.")
            return
        for i, post in enumerate(self.posts):
            print(f"\n#{i+1}\n{post}")
    def list_posts_by_author(self, author):
        filtered = [post for post in self.posts if post.author == author]
        if not filtered:
            print(f"🚫 Muallif '{author}'ning postlari topilmadi.")
            return
        for i, post in enumerate(filtered):
            print(f"\n#{i+1}\n{post}")
    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            removed = self.posts.pop(index)
            print(f"🗑️ '{removed.title}' o'chirildi.")
        else:
            print("❌ Noto'g'ri indeks!")
    def edit_post(self, index, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].edit_content(new_content)
        else:
            print("❌ Noto'g'ri indeks!")
    def show_latest_posts(self, count=3):
        if not self.posts:
            print("🚫 Hozircha postlar mavjud emas.")
            return
        latest_posts = self.posts[-count:]
        print(f"📢 So'nggi {len(latest_posts)} post:")
        for post in latest_posts:
            print(f"\n{post}")
    def main():
    blog = Blog()
    while True:
        print("\n=== Blog tizimi ===")
        print("1. Post qo'shish")
        print("2. Barcha postlarni ko‘rsatish")
        print("3. Muallif bo‘yicha postlarni ko‘rsatish")
        print("4. Postni o‘chirish")
        print("5. Postni tahrirlash")
        print("6. So‘nggi postlarni ko‘rsatish")
        print("7. Chiqish")
        choice = input("Tanlang (1-7): ")
        if choice == '1':
            title = input("Sarlavha: ")
            content = input("Kontent: ")
            author = input("Muallif: ")
            post = Post(title, content, author)
            blog.add_post(post)
        elif choice == '2':
            blog.list_all_posts()
        elif choice == '3':
            author = input("Muallif nomini kiriting: ")
            blog.list_posts_by_author(author)
        elif choice == '4':
            blog.list_all_posts()
            try:
                idx = int(input("O‘chiriladigan post raqamini kiriting: ")) - 1
                blog.delete_post(idx)
            except ValueError:
                print("❌ Raqam kiritilmadi!")
        elif choice == '5':
            blog.list_all_posts()
            try:
                idx = int(input("Tahrirlanadigan post raqamini kiriting: ")) - 1
                new_content = input("Yangi kontentni kiriting: ")
                blog.edit_post(idx, new_content)
            except ValueError:
                print("❌ Raqam kiritilmadi!")
        elif choice == '6':
            try:
                count = int(input("Necha ta so‘nggi postni ko‘rsatish: "))
                blog.show_latest_posts(count)
            except ValueError:
                print("❌ To‘g‘ri raqam kiriting!")
        elif choice == '7':
            print("✅ Dastur tugatildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov! 1-7 oralig‘ida tanlang.")
if __name__ == "__main__":
    main()
=== Blog tizimi ===
1. Post qo'shish
2. Barcha postlarni ko‘rsatish
3. Muallif bo‘yicha postlarni ko‘rsatish
4. Postni o‘chirish
5. Postni tahrirlash
6. So‘nggi postlarni ko‘rsatish
7. Chiqish
🚫 Hozircha postlar mavjud emas.

=== Blog tizimi ===
1. Post qo'shish
2. Barcha postlarni ko‘rsatish
3. Muallif bo‘yicha postlarni ko‘rsatish
4. Postni o‘chirish
5. Postni tahrirlash
6. So‘nggi postlarni ko‘rsatish
7. Chiqish
🚫 Hozircha postlar mavjud emas.
❌ Noto'g'ri indeks!

=== Blog tizimi ===
1. Post qo'shish
2. Barcha postlarni ko‘rsatish
...
5. Postni tahrirlash
6. So‘nggi postlarni ko‘rsatish
7. Chiqish
✅ Dastur tugatildi.

3)class Account:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    def display(self):
        return f"Hisob raqami: {self.account_number}, Egasi: {self.owner_name}, Balans: {self.balance} so'm"
      class Bank:
    def __init__(self):
        self.accounts = {}
    def add_account(self, account):
        if account.account_number in self.accounts:
            print("Bu hisob raqami allaqachon mavjud!")
            return False
        self.accounts[account.account_number] = account
        return True
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    def check_balance(self, account_number):
        account = self.get_account(account_number)
        return account.balance if account else None
    def deposit_to_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            return account.deposit(amount)
        return False
    def withdraw_from_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            return account.withdraw(amount)
        return False
    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if sender and receiver and sender.withdraw(amount):
            receiver.deposit(amount)
            return True
        return False
    def display_all_accounts(self):
        for acc in self.accounts.values():
            print(acc.display())
          def main():
    bank = Bank()
    while True:
        print("\n--- Bank Tizimi ---")
        print("1. Hisob qo'shish")
        print("2. Balansni tekshirish")
        print("3. Pul qo'yish (depozit)")
        print("4. Pul yechib olish")
        print("5. Pul o‘tkazish")
        print("6. Hisob ma’lumotlarini ko‘rsatish")
        print("7. Chiqish")
        tanlov = input("Tanlovni kiriting: ")
        if tanlov == "1":
            acc_num = input("Hisob raqamini kiriting: ")
            name = input("Hisob egasining ismi: ")
            boshlangich_balans = float(input("Boshlang‘ich balans: "))
            account = Account(acc_num, name, boshlangich_balans)
            if bank.add_account(account):
                print("Hisob muvaffaqiyatli qo'shildi.")
            else:
                print("Xatolik: Bu raqam bilan hisob mavjud.")
        elif tanlov == "2":
            acc_num = input("Hisob raqamini kiriting: ")
            balans = bank.check_balance(acc_num)
            if balans is not None:
                print(f"Balans: {balans} so'm")
            else:
                print("Hisob topilmadi.")
        elif tanlov == "3":
            acc_num = input("Hisob raqamini kiriting: ")
            amount = float(input("Depozit summasi: "))
            if bank.deposit_to_account(acc_num, amount):
                print("Pul muvaffaqiyatli qo'yildi.")
            else:
                print("Xatolik: Hisob topilmadi yoki noto‘g‘ri summa.")
        elif tanlov == "4":
            acc_num = input("Hisob raqamini kiriting: ")
            amount = float(input("Yechib olinadigan summa: "))
            if bank.withdraw_from_account(acc_num, amount):
                print("Pul muvaffaqiyatli yechildi.")
            else:
                print("Xatolik: Yetarli mablag‘ yo‘q yoki hisob topilmadi.")
        elif tanlov == "5":
            from_acc = input("Jo‘natuvchi hisob raqami: ")
            to_acc = input("Qabul qiluvchi hisob raqami: ")
            amount = float(input("O‘tkazma summasi: "))
            if bank.transfer(from_acc, to_acc, amount):
                print("Pul muvaffaqiyatli o‘tkazildi.")
            else:
                print("Xatolik: Hisoblardan biri mavjud emas yoki yetarli mablag‘ yo‘q.")
        elif tanlov == "6":
            print("\n--- Barcha Hisoblar ---")
            bank.display_all_accounts()
        elif tanlov == "7":
            print("Tizimdan chiqildi.")
            break
        else:
            print("Noto'g'ri tanlov! Qayta urinib ko'ring.")
          if __name__ == "__main__":
    main()
        --- Bank Tizimi ---
1. Hisob qo'shish
2. Balansni tekshirish
3. Pul qo'yish (depozit)
4. Pul yechib olish
5. Pul o‘tkazish
6. Hisob ma’lumotlarini ko‘rsatish
7. Chiqish
Hisob topilmadi.

--- Bank Tizimi ---
1. Hisob qo'shish
2. Balansni tekshirish
3. Pul qo'yish (depozit)
4. Pul yechib olish
5. Pul o‘tkazish
6. Hisob ma’lumotlarini ko‘rsatish
7. Chiqish

--- Barcha Hisoblar ---

--- Bank Tizimi ---
1. Hisob qo'shish
2. Balansni tekshirish
...
5. Pul o‘tkazish
6. Hisob ma’lumotlarini ko‘rsatish
7. Chiqish
Tizimdan chiqildi.
          
